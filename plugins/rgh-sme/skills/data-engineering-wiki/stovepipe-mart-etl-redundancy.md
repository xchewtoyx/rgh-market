---
type: concept
title: Stovepipe Data Mart ETL Redundancy
description: >
  Why letting independent data marts proliferate without a shared repository
  multiplies ETL load on source systems and produces contradictory numbers
  across marts.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Adamson), ch. 2"
---

A **stand-alone data mart** — an analytic store built for one subject area
with no shared enterprise repository behind it — is often the fastest, cheapest
path to a working report: no time spent reconciling cross-team definitions of
shared entities like "customer" first. They accumulate for ordinary reasons:
a purchased packaged application ships with its own mart, a legacy system
predates any later enterprise data effort, a team builds one outside a formal
IT process, or one arrives bundled in an acquisition.

The pipeline-engineering cost only shows up once more than one such mart
exists side by side, independently extracting from the same source systems —
a pattern earning the pejorative label **stovepipe**:

- **Redundant extraction load**: each mart runs its own ETL against the same
  source systems, multiplying the [source-system read
  impact](source-system-evaluation.md) that a single shared extraction would
  have paid once.
- **Divergent business rules on the same source data**: independently built
  ETL processes applying slightly different transformation or cleaning logic
  to the same underlying facts produce genuinely contradictory numbers across
  marts — not a rounding difference, but two departments' reports
  disagreeing about what should be the same figure, with no reconciliation
  path between them.
- **No shared repository for granular data**: because each mart only loads
  what its original scope anticipated, a new question that needs more detail
  than any one mart retained has nowhere to be answered from — the detail
  was never centrally kept anywhere.

None of this is a defect of dimensional modeling technique itself — a
stand-alone mart's star schema works exactly as designed within its own
scope. The failure is architectural: no shared extraction, no
[conformed](conformed-dimension-publish-subscribe.md) definitions across
marts, and no [master data management](master-data-management.md) tying the
same real-world entity together across them. A stand-alone mart is still a
reasonable choice when a team explicitly accepts the future
reconciliation cost it's taking on — the problem is only proliferating them
*without* that being a conscious, named trade-off.

Two named architectures are the disciplined, intentional answers to this
same failure mode, solving it in opposite directions — see
[Kimball bus vs. Inmon CIF](kimball-bus-vs-inmon-cif-architecture.md).
