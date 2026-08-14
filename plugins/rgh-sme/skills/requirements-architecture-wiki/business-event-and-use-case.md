---
type: concept
title: Business Event and Business Use Case
description: >
  Partitioning a business domain by the external events it must respond
  to, rather than by guesswork, gives each unit of requirements work a
  natural, independent, traceable boundary.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 4"
---

A **business event** is something that happens outside the boundary of
the business "work" — or a significant passage of time — that demands a
response: an external entity doing something (a customer places an
order), or a temporal trigger (a scheduled nightly audit). A **business
use case (BUC)** is the complete response the work makes to a single
business event: every activity, decision, and data flow from the moment
the event occurs until the work returns to rest.

To identify BUCs: inspect the [context diagram](context-diagram.md) and
examine each incoming data flow, trace it back to the event that actually
caused it, group inputs triggered by the same event into one response, and
list the results as a business event list mapped one-to-one to BUCs.

Partitioning this way, rather than by guessing at natural-seeming feature
groupings, gives each BUC useful properties: cohesion (each one is a
single, independent business responsibility), a manageable size for
estimation and assignment, and clean traceability, since requirements,
test cases, user stories, and code can all be mapped back to the specific
BUC that motivated them — see [requirements
traceability](requirements-traceability.md). Within the [scope of the
product](scope-of-work-vs-scope-of-product.md), a single BUC is often
served by multiple product use cases (PUCs) — the user- or system-facing
interactions that implement part or all of the BUC.
