---
type: concept
title: Backpressure and Handshaking
description: Instead of a downstream resource silently absorbing (or being crushed by) whatever rate an upstream sender chooses, backpressure lets the downstream signal its real capacity so the upstream can slow down before overload, rather than after.
sources:
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 5"
---

Most capacity-protection patterns react after a resource is already under stress — a [circuit breaker](circuit-breaker-pattern.md) trips once errors start, [load shedding](adaptive-throttling.md) drops requests once a queue is already full. **Backpressure** and **handshaking** instead let a downstream component communicate its available capacity to an upstream sender *before* it is overwhelmed, so the sender can slow its own emission rate proactively rather than continuing to push at a rate the downstream cannot sustain.

## Two Related Mechanisms

*   **Handshaking:** client and server negotiate capability or workload before a request is sent — the server exposes a capacity or health signal (a custom response header, a health-check status) that the client consults and honors when deciding how much work to send next.
*   **Backpressure:** a more mechanical, often protocol-level version of the same idea — a downstream queue or buffer that is filling up signals the upstream to slow down, the way TCP receive-window advertisements throttle a sender to a receiver's actual buffer capacity, or the way reactive-streams-style flow control lets a slow consumer pull data at its own pace instead of a fast producer pushing faster than the consumer can process.

## Why This Beats Purely Reactive Protection

A purely reactive pattern (shed load once overloaded, trip a breaker once errors appear) accepts that the system will briefly *become* overloaded before it responds. Backpressure and handshaking instead keep the sender's rate matched to the receiver's real capacity continuously, so the overload condition that would trigger those reactive patterns is less likely to occur in the first place. The trade-off is that backpressure requires both ends of a call to cooperate — a sender that ignores the downstream's signal, or an upstream link with no mechanism to carry one, gets none of this protection and falls back to needing the purely reactive patterns instead.

## Relationship to Adjacent Patterns

Backpressure is the proactive counterpart to [concurrency limiting as admission control](concurrency-limiting-as-admission-control.md): admission control is the downstream unilaterally capping how much concurrent work it accepts, queuing or rejecting the rest; backpressure instead communicates the downstream's state back to the sender so the sender adjusts its own rate, avoiding the queueing delay or rejection admission control would otherwise impose. Systems that support genuine end-to-end backpressure — a message queue with consumer-driven pull semantics, an async pipeline with propagated flow control — can absorb demand variability with less need for the reactive load-shedding patterns further down the chain.
