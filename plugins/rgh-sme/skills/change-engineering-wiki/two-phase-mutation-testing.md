---
type: concept
title: Two-Phase Mutation Testing
description: >
  Split a pipeline's write into a proposal phase and a validated-apply
  phase so a canaried change's real output can be checked for correctness
  before it is actually committed to the destination.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 13"
---

# Two-Phase Mutation Testing

For batch and streaming pipelines, [canary release](canary-release.md) runs
into a problem request/response services don't have: a pipeline's output is
often a durable mutation (a write to a downstream store), and you cannot
cleanly "throw away" a canary's output the way you can drop an HTTP
response from a canaried request.

Two-phase mutation testing solves this by splitting the write into two
steps: a read-and-transform phase writes its *proposed* mutation to a
temporary store, and a separate validation step checks the proposal for
correctness; only mutations that pass validation are applied to the real
destination in a second pipeline phase. This lets a canary of a pipeline
change be evaluated against its actual real-world output, without polluting
the destination if the canary is wrong.

See [canarying pipeline systems](canarying-pipeline-systems.md) for the
other adjustments canary evaluation needs for batch/async systems (duration
spanning a full work unit, isolation by worker pool).
