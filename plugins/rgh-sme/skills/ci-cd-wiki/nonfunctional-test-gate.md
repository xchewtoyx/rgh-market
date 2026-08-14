---
type: concept
title: Nonfunctional Test Gate
description: >
  A dedicated deployment-pipeline stage that automates capacity, load, stress,
  soak, and spike testing against a production-like environment, so
  performance and scalability regressions are caught before release rather
  than discovered in production.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 9"
---

# Nonfunctional Test Gate

Nonfunctional requirements (NFRs) — capacity, throughput, latency,
concurrency, availability, scalability — are exactly the [agile testing
quadrants](agile-testing-quadrants.md)' Q4 (technology-facing, critique the
product). A [deployment pipeline](deployment-pipeline.md) needs an explicit
stage for this quadrant because functional acceptance tests (Q1) do not
exercise it: a build can be functionally correct and still fail under load.

## Taxonomy of capacity tests

- **Performance baseline testing**: measures latency and resource consumption
  under normal expected load, to establish a comparison point for later runs.
- **Load testing**: verifies throughput and response-time SLAs hold under
  maximum expected peak load.
- **Stress testing**: pushes the system beyond expected capacity to find its
  breaking point, failure modes, and whether it recovers afterward.
- **Endurance / soak testing**: sustains load for an extended period (24–72
  hours) to surface slow leaks — memory, thread pools, DB connections, log
  disk usage — that only appear over time.
- **Spike testing**: evaluates stability and auto-scaling response to sudden,
  large traffic spikes.

## Running it as a pipeline stage

The gate runs after the [commit stage](commit-stage.md) and acceptance tests
pass, deploying the build to a
[capacity test environment](capacity-test-environment-fidelity.md) and
executing an automated load script. See
[performance regression gate](performance-regression-gate.md) for how results
are compared against baseline to decide pass/fail automatically.

When the loads worth testing exceed what the environment or licensed
load-generation tooling can actually produce, extrapolating from a small set
of real measurements — see
[virtual load testing via scalability extrapolation](virtual-load-testing-via-scalability-extrapolation.md)
— can substitute for building out full-scale capacity infrastructure.
