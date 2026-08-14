---
type: concept
title: Measuring Infrastructure Team Workflow Effectiveness
description: Using the four key delivery metrics as SLIs/SLOs to evaluate an infrastructure team's workflow, and using value stream mapping to target improvement effort at the actual bottleneck rather than the most visible one.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 20"
---

The [four key delivery and stability metrics](four-key-delivery-metrics.md) give an infrastructure team a concrete basis for its own Service Level Indicators (what to measure), Service Level Objectives (internal targets), and Service Level Agreements (external commitments) for its delivery workflow — what specifically to measure depends on the team's own context and what it's trying to improve.

**Value stream mapping** is the tool for finding where effort is actually worth spending: it breaks a change's total lead time down by activity, including time spent waiting, so improvement effort goes toward the biggest real bottleneck rather than the most visibly inefficient-looking step. A team that cuts server-provisioning time from eight hours to ten minutes has made a dramatic 98% improvement to that one step — but if the request that triggers provisioning typically waits ten days in a queue first, the total lead time only improves by about 10%. Measuring end-to-end lead time (and other metrics, like failure rate) while making changes is what prevents a team from locally optimizing one stage while making the overall flow worse.

This measurement discipline is what makes it possible to evaluate whether a specific design choice — how [stacks are sized](monolithic-stack-antipattern.md), how [dependencies are integrated](build-time-project-integration-pattern.md), how [governance is embedded in the pipeline](governance-in-pipeline-based-workflow.md) — is actually paying off, rather than assuming it must be an improvement because it seems more sophisticated.
