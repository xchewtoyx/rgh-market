---
type: concept
title: Batch vs. Streaming Workflow Processing
description: >
  Decide separately from topology whether a workflow processes a known finite
  set of work items together or an ongoing stream as items arrive.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

Independent of [workflow topology](workflow-topology.md) (how tasks connect),
decide whether a workflow processes work items in **batch** — a known, finite
set, processed together — or **streaming** — an arbitrary or ongoing number of
items created or retrieved as the workflow runs. The same workflow can often
go either way: a marketing-email workflow over a list of storefronts could run
batch (collect a storefront list, then process it) or streaming (a web
crawler continuously discovers storefronts and processes each as it arrives).

Batch is typically simpler to set up and maintain, and efficient for large
known volumes. Streaming suits real-time, low-latency needs but is more
complex to build and operate. Choose based on whether the workload is
naturally bounded-and-known ahead of time or open-ended and arrival-driven,
not based on topology.
