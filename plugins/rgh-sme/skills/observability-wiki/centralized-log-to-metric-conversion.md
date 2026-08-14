---
type: concept
title: Deriving Metrics from Centralized Logs
description: Once logs are centralized in a common event router, counting occurrences of a specific log pattern turns it into a metric time series, enabling statistical anomaly detection on events that were never explicitly instrumented as a counter.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14"
---

When logs from across the whole infrastructure land in a common event router rather than sitting in per-server files, a specific log line (e.g. "child pid 14024 exit signal Segmentation fault") can be counted across the entire fleet to produce a derived counter metric — a segfault-rate time series — without the original code ever having been instrumented to emit that metric directly.

This makes statistical techniques available retroactively: an alert like "ten segfaults last week" escalating to "thousands of segfaults in the last hour" becomes possible purely from log volume, even for failure modes nobody anticipated when the logging statements were written. This is one of the practical benefits of a **unified event router/pipeline** architecture (collection → routing → visualization/alerting) over siloed, single-purpose logging — see [telemetry pipeline stages](telemetry-pipeline-stages.md) for the fuller architecture this fits into.
