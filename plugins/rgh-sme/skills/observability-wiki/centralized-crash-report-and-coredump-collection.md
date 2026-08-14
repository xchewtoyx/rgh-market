---
type: concept
title: Centralized Crash Report and Coredump Collection
description: Every process crash should generate a crash report (resource stats at time of death, stack traceback) and, where feasible, a coredump, collected automatically to a central store before the evidence disappears — enabling both simple crash-rate metrics and cross-machine pattern analysis that can surface shared-library, OS, or hardware bugs invisible from any single crash.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
---

A crashed process is a perishable source of debugging evidence: the crash report (resource utilization and a stack traceback at the moment of death) and, where the runtime supports it, a full memory coredump are only available for a limited window before the disk is reclaimed, the machine is recycled, or a log-rotation policy deletes them. Automated, centralized collection — shipping this data off the crashing machine as part of the crash-handling path itself, rather than relying on someone noticing and pulling it manually — is what keeps this evidence available for actual use.

Centralizing collection unlocks two distinct kinds of value beyond debugging any single incident: first, aggregate crash-rate metrics per service/version become possible at all, feeding directly into [using an exception collector as a rollout health signal](exception-collector-as-rollout-health-signal.md); second, and easy to miss, cross-machine pattern analysis across the whole fleet can surface bugs that no single crash report would reveal on its own — a bug confined to a specific shared library version, a specific OS kernel version, or even a specific hardware/CPU revision only becomes visible once traces from many machines are compared side by side. A crash rate that looks like unrelated background noise machine-by-machine can resolve into a sharp, actionable signal once aggregated.

This is the same underlying discipline as [structured wide events](structured-events-as-observability-substrate.md) applied to the crash path specifically: capture rich context at the moment something goes wrong, in a form durable and structured enough to support both an immediate look and a later cross-cutting query.
