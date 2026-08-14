---
type: concept
title: Stable vs. Dynamic Instrumentation Points
description: Instrumentation probe points trade stability for coverage — statically pre-defined probes (tracepoints, USDT) survive version upgrades but only exist where developers put them, while dynamic probes (kprobes, uprobes) can attach almost anywhere but are fragile against internal changes.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 4"
---

When deciding what to instrument, there's a recurring trade-off between coverage and stability:

- **Static/stable probes** — tracepoints compiled into kernel source at fixed locations, or User Static Defined Tracing (USDT) macros embedded in user applications (e.g. PostgreSQL, the JVM, Node.js). Pros: stable API across version upgrades, guaranteed low overhead, because they're placed and maintained deliberately. Cons: only exist at the specific locations someone chose to instrument in advance.
- **Dynamic probes** — kprobes/kretprobes (kernel function entry/return) and uprobes/uretprobes (user-space function entry/return) can attach to almost any symbol without recompilation. Pros: near-total visibility, including into code you don't control. Cons: depend on internal function names/signatures that can change between releases, so a dynamic probe written against one version may silently stop working (or attach to the wrong thing) after an upgrade; user-space probes additionally carry meaningfully higher per-hit overhead than kernel probes because of the user-to-kernel context-switch and breakpoint-trap handling involved.

The practical implication: build durable dashboards and alerts on stable probes/semantic conventions, and reach for dynamic probes as an investigative tool for one-off debugging sessions rather than as the backbone of standing telemetry — see [observability tool selection by scenario](observability-tool-selection-by-scenario.md).
