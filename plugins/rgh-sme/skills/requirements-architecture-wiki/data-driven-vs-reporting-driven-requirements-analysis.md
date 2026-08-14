---
type: concept
title: Data-Driven vs. Reporting-Driven Requirements Analysis
description: >
  Two opposite traditional strategies for discovering data-warehouse
  requirements — modeling the source data versus interviewing report
  consumers — each fail in a characteristic way when used alone, which is
  why most warehouse initiatives combine both.
sources:
  - title: Agile Data Warehouse Design
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 1, pp. 11-13"
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (James Serra), ch. 15"
---

Building a data warehouse always requires some [requirements
analysis](requirements-elicitation-techniques.md) before database design
techniques (3NF entity-relationship modeling, or [dimensional
modeling](dimensional-modeling-four-step-elicitation.md)) can start.
Historically this split into two opposite strategies, and each has a
characteristic failure mode when relied on exclusively.

**Data-driven (supply-driven) analysis** discovers requirements by
analyzing the operational source data itself — re-modeling multiple source
systems via entity-relationship techniques into one comprehensive model —
while avoiding business-stakeholder involvement until afterward. Without
user input to prioritize and scope the result, this produces designs that
are slow and expensive to build, biased toward the operational (OLTP)
system's own perspective rather than the business's analytical needs, hard
to query, and rarely answer the questions the business actually has. This
is the "build it and they will come" or "field of dreams" approach. It
persists because it stays within IT's technical comfort zone and avoids
heavy stakeholder engagement, and it has grown more problematic as
operational data models — especially generic packaged-application schemas
such as ERP systems — have grown more complex to reverse-engineer. See
[architecturally significant requirement](architecturally-significant-requirement.md)
for why a design derived from data structure rather than from stated
business need routinely misses the requirements that actually matter to
the business.

**Reporting-driven (demand-driven) analysis** discovers requirements by
interviewing BI stakeholders individually or in small groups about their
reporting needs, consolidating interview notes and report mock-ups into a
source-verified requirements list, and ratifying it with stakeholders
before design begins. Done well and with scope managed carefully, this
produces timely, targeted deployments. Its characteristic failure is
different: detailed analytical requirements are **accretive** — they build
up layer upon layer, and a BI user typically cannot articulate what they
will need next until they have the answers the *next* set of reports would
give them — so getting stakeholders to describe requirements beyond "the
next report" takes real skill, and collating, ratifying, and gaining
sign-off across enough stakeholders for an enterprise-wide view can be
extremely slow. A second-order failure compounds this: an inexperienced
modeler who matches the design too tightly to the exact reports requested,
instead of treating those reports as clues pointing at the underlying
business process that needs modeling in fuller detail, produces a design
that cannot flex as requirements evolve — a problem that is *not* inherent
to [dimensional modeling](dimensional-modeling-four-step-elicitation.md)
itself (a common but misleading industry critique), but to reverse-
engineering from report requests instead of modeling the business process
at atomic grain.

The data-driven failure mode has a durable, practical symptom worth
naming on its own: a warehouse whose structure mirrors the shape of its
operational source systems rather than the business processes and KPIs it
is meant to report on. Operational systems aren't designed for analysis,
so mirroring their structure risks missing insights the business actually
needs; it also means an unrelated change to an operational system forces
rework of the warehouse, producing ongoing instability that has nothing to
do with any real business requirement. The fix is the same one this
concept's data-driven/reporting-driven framing already implies: structure
the warehouse by business need — discovered from stakeholders, not
reverse-engineered from a source schema — even when the underlying
analysis started from the operational data.

**In practice, most modern warehouse initiatives combine both approaches**:
early, purely data-driven enterprise warehouses biased toward source-data
analysis; more recent dimensional warehouses and marts bias toward
reporting-driven analysis; neither extreme is reliable alone. See
[proactive requirements analysis](proactive-requirements-analysis.md) for
a third strategy that addresses a limitation both of these share — both
assume real operational data or existing reports already exist to analyze.
