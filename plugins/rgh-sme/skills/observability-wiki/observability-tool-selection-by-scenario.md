---
type: concept
title: Observability Tool Selection by Scenario
description: Observability tooling falls into distinct categories by when and why you'd reach for it — static pre-execution inspection, crisis triage, continuous trend monitoring, and dynamic tracing — and matching the category to the situation matters more than knowing every individual tool.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 4"
---

Four broad categories of observability tooling, distinguished by when you'd reach for each:

1. **Static performance tools** — inspect configuration, hardware capability, topology, and build limits *before* active execution (e.g. `lscpu`, `/proc/cpuinfo`, `numactl --hardware`). Used to understand what a system's ceiling even is, before looking at runtime behavior.
2. **Crisis tools** — emergency triage tools that are pre-installed with minimal dependencies, used during an active production incident to quickly assess host resource health under severe degradation (e.g. `top`, `vmstat`, `iostat`, `dmesg`). Optimized for being available and fast to run, not for depth.
3. **Continuous system monitoring tools** — engines that record counter and gauge time series over historical windows, for trend analysis, capacity planning, and automated alert triggering (e.g. Prometheus, `node_exporter`, OpenTelemetry). This is the category most dashboards and alert rules are built on — see [purposes of monitoring](purposes-of-monitoring.md).
4. **Dynamic tracing tools** — event-driven instrumentation of arbitrary execution points across kernel and user space, with zero recompilation (`perf`, Ftrace, BPF-based tools). Reached for when the first three categories can't answer a specific "why is this one request/thread doing this" question — this is the domain of [tracing and profiling](fixed-counters-vs-profiling-vs-tracing.md).

None of these categories replaces another: crisis tools answer "is this host okay right now," continuous monitoring answers "was this normal an hour/week ago," and dynamic tracing answers "what exactly is this specific slow thing doing." Picking the wrong category for the question at hand (e.g. reaching for a heavyweight tracer during a live outage, or relying on crisis tools to catch a slow trend) wastes time under pressure.
