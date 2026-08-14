---
type: concept
title: Data-Flow Style
description: >
  Data-flow styles move data through a sequence of transformations —
  batch sequential, pipe-and-filter, and process-control variants — and
  documentation must cover format, buffering, ordering, and error
  propagation between stages.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

Data-flow is a [component-and-connector style](component-and-connector-view.md)
in which components transform streams of data passed between them.
Variants include batch sequential (each stage completes fully before the
next starts), pipe-and-filter (stages run concurrently, streaming data
through), and process-control (feedback-driven, often with a control loop
adjusting a physical or logical process). These styles favor reuse of
individual stages, incremental processing, and throughput, since a stage
can often be replaced or added without touching its neighbors.

That reuse benefit only holds if the documentation states the things that
make stages composable: the data format each stage expects and produces,
how buffering works between stages (and what happens if a downstream stage
is slower than an upstream one), what ordering guarantees exist across the
stream, and how an error at one stage propagates — does it halt the
pipeline, get logged and skipped, or get retried? Without these, "pipeline
of stages" is a shape, not an architecture that can be reasoned about.
