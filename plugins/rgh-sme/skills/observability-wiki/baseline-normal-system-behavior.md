---
type: concept
title: Establish a Baseline for Normal System Behavior
description: Debuggers often waste time investigating behavior that turns out to be expected; comparing against a baseline of the system's behavior when it wasn't suspected of a problem is the way to tell "weird but normal" apart from "actually the bug."
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

It's common to start debugging what turns out to be entirely expected system behavior — a shutdown routine that logs an `abort()` call as its last, intentional step; a browser resolving deliberately-random DNS names to test for tampering. These look suspicious in isolation but are normal once you know the system's baseline.

Establishing that baseline can happen two ways: proactively, by characterizing behavior when you don't suspect any problem, or retroactively, by examining historical logs/metrics from before the current problem began. A concrete example: a serious bug caused many out-of-memory conditions on a given day, but comparing that count against two weeks of historical data showed the system has many OOM conditions *every* day — the metric in question wasn't actually informative for this particular bug, even though the bug was real and needed fixing via other evidence.

A related trap is **normalizing deviance**: a bug or inefficiency becomes accepted as "just how the system behaves" over time, and stops being questioned even though it's a real, fixable problem (e.g. a server that had "always" spent ~10% of memory on heap fragmentation, until someone actually looked). Rotating people through on-call, listening to newcomers who haven't yet absorbed the folklore, and periodically re-examining old assumptions are practical countermeasures. See [outlier detection vs. threshold alerting](outlier-detection-vs-threshold-alerting.md) for an automated, continuous version of baseline comparison.
