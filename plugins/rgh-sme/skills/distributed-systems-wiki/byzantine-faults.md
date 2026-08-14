---
type: concept
title: Byzantine Faults
description: >
  The fault model where nodes may lie or act maliciously — expensive to
  tolerate, and usually the wrong model for private datacenters.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
---

# Byzantine Faults

Most distributed algorithms assume nodes are **honest but unreliable**: they
may crash, stall, or lose messages, but when they respond they follow the
protocol truthfully. A **Byzantine fault** breaks that assumption — a node
sends corrupted or deliberately false messages (the "Byzantine Generals
Problem"). Byzantine fault tolerance (BFT) requires agreement among more than
two-thirds of nodes and carries substantial protocol overhead.

When BFT matters: aerospace (radiation-flipped memory), and open peer-to-peer
networks where participants are mutually untrusting (blockchains). In a
private datacenter where you control all nodes, full BFT is almost never worth
it — and it wouldn't help against the common enemy anyway (an attacker who
compromises one node can usually compromise all, since they run the same
software).

What *is* worth doing everywhere is cheap protection against "lying" that
arises from bugs and corruption rather than malice: checksums on network
messages (hardware bit-flips slip past TCP's checksum surprisingly often),
input sanitization on anything user-supplied, and cross-checking values from
multiple sources (e.g. NTP clients query several servers). These
weak-Byzantine defenses catch most real-world corruption at a fraction of BFT's
cost. The fault model chosen belongs in the algorithm's explicit
[system model](system-models.md), and continual
[self-auditing](timeliness-vs-integrity.md) — background scanners, recompute-
and-compare on derived state — covers what the model missed.
