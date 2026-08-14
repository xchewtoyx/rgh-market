---
type: concept
title: Periodically Audit for Unjustifiably Disabled Telemetry
description: Instrumentation that got turned off — usually from an unverified fear of performance overhead — quietly reopens the exact blind spot the instrumentation existed to close, so it's worth periodically auditing for disabled telemetry and checking whether the original concern actually holds up under measurement.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §3.2"
---

Instrumentation that exists but gets disabled is a distinct failure mode from instrumentation that was never added — [closing telemetry gaps from past incidents](closing-telemetry-gaps-from-past-incidents.md) covers finding and filling gaps that never had coverage, but a service owner turning off tracing or logging that already existed reopens a gap that was previously closed, often silently and without anyone else noticing.

The recurring root cause is an unverified fear of overhead: a service owner disables tracing because they *believe* it's too expensive, not because they measured it and confirmed it was. The fix isn't to forbid disabling telemetry — sometimes it genuinely is too expensive for a specific hot path — it's to make disabling it visible and revisited rather than permanent-by-default. Google's practice with Dapper: run occasional audits specifically looking for configurations where tracing had been turned off, and when found, re-investigate the original overhead concern with real measurement rather than taking it on faith. In practice, essentially every case they found had the underlying overhead concern turn out to be immaterial once actually measured, and tracing was turned back on.

This is worth pairing with [keeping unsampled instrumentation overhead negligible](unsampled-instrumentation-overhead-must-be-near-zero.md) in the first place — the fewer legitimate reasons there are to disable instrumentation for overhead, the more confidently an audit can treat "disabled" as a signal worth investigating rather than a defensible engineering decision to leave alone.
