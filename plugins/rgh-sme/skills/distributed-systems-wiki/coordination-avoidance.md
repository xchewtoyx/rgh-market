---
type: concept
title: Coordination Avoidance
description: >
  Many business "constraints" are actually loose — violations can be
  apologized for and compensated — which lets systems skip synchronous
  consensus for throughput, latency, and cross-region availability.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

# Coordination Avoidance

Enforcing a hard constraint at write time — a truly unique username, a
never-negative balance — requires synchronous agreement:
[consensus](consensus.md) or a [linearizable](linearizability.md)
compare-and-set, with their latency and partition-unavailability costs. But
before paying that, ask whether the constraint is actually hard.

Most businesses already operate with **loosely interpreted constraints**:
airlines overbook and rebook with vouchers; warehouses sell out-of-stock
items and backorder; banks allow overdrafts and charge fees. The pattern is
*apology-based*: accept the write optimistically, detect the violation
asynchronously, repair with a **compensating transaction** and an apology
workflow. The cost of an occasional apology is often far below the cost of
coordinating every operation.

A coordination-avoiding design combines this with
[integrity-preserving dataflow](timeliness-vs-integrity.md): the log
guarantees nothing is lost or double-applied, while constraints are checked
asynchronously and violations handed to compensation logic. The reward is
higher throughput, low latency, and the ability to run active in multiple
regions without cross-region coordination on the hot path — coordination is
reserved for the few constraints (if any) where an apology is genuinely
unacceptable.

The design question to ask of every "must" in a requirements doc: *what
actually happens if this is briefly violated?* If the honest answer is "we'd
send an email and fix it", it doesn't need consensus.
