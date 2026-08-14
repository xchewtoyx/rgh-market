---
type: concept
title: Flow Metrics
description: >
  Five metrics (velocity, efficiency, time, load, distribution) for
  diagnosing a value stream's health beyond a single lead-time number,
  distinguishing "is delivery accelerating" from "is delivery efficient."
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 1"
---

# Flow Metrics

Drawn from Mik Kersten's Flow Framework, as a warning against proxy metrics
(raw lines of code, deployment frequency in isolation) that show local
optimization without telling you whether business value is actually moving
faster. Five complementary metrics, useful together in
[value stream mapping](value-stream-mapping.md):

- **Flow velocity**: number of flow items (work items) completed per time
  period — is value delivery accelerating?
- **Flow efficiency**: proportion of a flow item's total elapsed time that was
  actively worked, versus waiting — the process-time/lead-time ratio applied
  per item; reveals how much of [cycle time](cycle-time.md) is queue time
  versus real work.
- **Flow time**: elapsed time for a unit of business value (feature, defect,
  risk item, debt item) to move through the whole value stream — is
  time-to-value shrinking?
- **Flow load**: number of active or waiting flow items at once, a WIP
  analogue — high flow load signals demand outweighing capacity, predicting
  reduced velocity and increased flow time before those show up directly. See
  [capacity utilization and lead time](capacity-utilization-antipattern.md)
  for why high load degrades lead time.
- **Flow distribution**: the proportion of each flow-item type (features,
  defects, risk items, debt items) in the stream — tunable to make sure the
  stream isn't being consumed entirely by one category (e.g. all defect
  remediation, none of it feature work).

Where [the DORA four key metrics](dora-four-key-metrics.md) tell you whether
delivery performance is good overall, flow metrics help decompose *why*, by
separating "how much is moving" (velocity, distribution) from "how well it's
moving" (efficiency, load) from "how long any one thing takes" (flow time).
