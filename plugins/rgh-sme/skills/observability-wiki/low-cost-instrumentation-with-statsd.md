---
type: concept
title: Making Instrumentation a One-Line Change
description: If adding a new metric requires meaningful effort, engineers will skip it; tools like StatsD reduce instrumenting a code path to a single line, which measurably increases how much of a codebase actually gets instrumented.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14"
---

StatsD (created and open-sourced at Etsy) established a philosophy: creating a new production metric should be as low-friction as a single line of code, comparable to adding a `print` statement rather than a database schema change. A call like `StatsD::increment("login.successes")` is enough to generate a login-success/failure graph, typically rendered through Graphite or Grafana.

The underlying claim is that instrumentation *friction*, not developer indifference, is the main reason codebases end up under-instrumented — if it's a hassle, people rationally skip it under time pressure, and the resulting blind spots only get discovered during an incident. This same principle motivates OpenTelemetry's push toward telemetry being *native* to libraries and frameworks (see [context propagation](context-propagation.md)) rather than something bolted on after the fact, and the [instrumentation litmus test](instrumentation-litmus-test.md) for what to add on every change.
