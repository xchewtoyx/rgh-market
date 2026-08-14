---
type: concept
title: Uptime vs Availability vs Reliability
description: >
  Three commonly conflated terms with precise, distinct meanings that matter
  when choosing what an SLI actually measures.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 2, ch. 3"
---

- **Uptime** — is the service process actually running?
- **Availability** — can the service actually respond to requests?
- **Reliability** — is the service actually performing the duties it was
  designed to do?

Each is a strictly narrower question than the last: a process can be up but
unable to respond (not available); a service can respond but return the
wrong answer or unacceptable quality (available but not reliable).
Reliability is the property that actually matters to users — see
[user-centric SLI selection](user-centric-sli-selection.md) — so an SLI set
built only around uptime or availability risks missing real user pain even
while "looking green."

See also [time-based vs request-based availability](time-based-vs-request-based-availability.md)
for the two common ways of turning "availability" itself into a computable
ratio.
