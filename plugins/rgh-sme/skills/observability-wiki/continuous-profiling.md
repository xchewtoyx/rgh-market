---
type: concept
title: Continuous Profiling
description: Running profiling agents always-on rather than only during an incident is affordable because profile data compresses well (call patterns repeat), and it turns profiling from a reactive incident-response tool into a routine telemetry stream that can be queried retroactively.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 20"
---

[Profiling](fixed-counters-vs-profiling-vs-tracing.md) is traditionally reached for reactively — attached to a specific process during an active incident, then torn down afterward. **Continuous profiling** instead runs profiling agents (or scrapes `pprof`-style endpoints) all the time, as a standing telemetry stream rather than a one-off diagnostic. This is affordable because profile data compresses unusually well — call patterns repeat heavily across samples — so the marginal cost of retaining a much longer window is low relative to the value of being able to look backward at CPU behavior *before* you knew there was a problem, rather than only from the moment someone attached a profiler.

This mirrors the shift from crisis-only tooling to standing telemetry described in [observability tool selection by scenario](observability-tool-selection-by-scenario.md) — the same profiling technique, made continuous, moves from a "crisis tool" into the "continuous monitoring" category. It's a concrete enabler of [profiling and tracing being complementary](profiling-vs-tracing-complementary.md): with continuous profiling already running, a trace-identified anomaly can be immediately cross-referenced against profile data for the same time window, without having to reproduce the problem live first.
