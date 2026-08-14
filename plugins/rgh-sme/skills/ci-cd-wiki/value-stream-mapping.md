---
type: concept
title: Value Stream Mapping
description: >
  Tracing the full sequence of activities a change passes through from
  conception to production-delivered-value, used to locate where delivery time
  is actually being lost.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1"
---

# Value Stream Mapping

A value stream is the full sequence of activities required to take a feature,
change, or fix from initial conception through development, testing, and
deployment to the point it delivers value to users. Mapping it — listing each
stage a change actually passes through and measuring [process time versus queue
time](cycle-time.md) at each one — is how a team finds the actual bottleneck in
its delivery pipeline rather than guessing.

This is the diagnostic counterpart to [cycle time](cycle-time.md): cycle time
is the number that says something is slow; value stream mapping is how you
find out which stage is slow and why (e.g. waiting for a shared test
environment, a manual approval queue, or a slow [commit stage](commit-stage.md)).
Continuous improvement of the delivery process depends on repeating this
mapping regularly rather than treating the pipeline's stage boundaries as
fixed.
