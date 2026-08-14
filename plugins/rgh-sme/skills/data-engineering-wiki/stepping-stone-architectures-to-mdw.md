---
type: concept
title: Stepping-Stone Architectures Toward a Modern Data Warehouse
description: >
  Three interim architectures — EDW augmentation, a lake used only as
  staging, and lake-only — that let an organization keep deriving value from
  data while migrating toward a full modern data warehouse.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 10"
---

Building a full [modern data warehouse](modern-data-warehouse-architecture.md)
(MDW) is a long, resource-intensive migration. Rather than a big-bang cutover,
an organization typically passes through one of a few interim architectures
that are still useful destinations in their own right, not just placeholders —
each is a legitimate stepping stone whose migration path leads naturally
toward a full MDW.

**EDW augmentation**: a long-standing on-prem
[relational data warehouse](data-warehouse-architecture.md) that can't handle
big data — storage limits, compute limits, too short a maintenance window,
no semi-structured support — gets a cloud [data lake](data-lake-architecture.md)
added alongside it. Big data lands and gets queried in the lake; the EDW
keeps its existing data and workload untouched. This adds capacity without
touching what already works, but existing query tools may not reach the
lake, cleaning lake data needs new compute and skills, and the EDW's own
workload is never offloaded. Migration path: begin a phased on-prem-to-cloud
migration of the EDW's own data into the lake once the big-data side is
proven out.

**Temporary lake as staging only**: when transforming big data inside the
EDW itself would take too long, the lake is used purely as staging/refining
space — not for querying or reporting, which stays entirely in the EDW.
Data may flow EDW → lake → refine → back to EDW. This narrow scope (no
reporting workload against the lake) lets it be stood up fast and eases the
EDW's maintenance-window strain, at the cost of not getting any of a full
lake's other benefits (ML training surface, schema-on-read flexibility for
new source types). With a few modifications — opening the lake up to direct
querying — this evolves cleanly into a full MDW, making it the most direct
stepping stone of the three.

**All-in-one (lake-only)**: all reporting and querying happens directly
against the lake; no RDW exists yet. This is fastest to stand up and suits
startups, prototyping, or user bases that are primarily technical (e.g.,
data scientists who don't need warehouse-grade tooling) — the same profile
[the lake-only vs. RDW-second decision](lakehouse-vs-warehouse-copy-decision.md)
weighs more generally. It trades away query performance, mature security
controls, referential integrity, and general-user friendliness. For some
audiences this is fine as a permanent state; becoming a stepping stone toward
an MDW means adding an RDW on top later, at which point the architecture
converges with the modern data warehouse pattern.

Which stepping stone fits depends on what's actually broken about the
current setup: capacity/format limits with a workload worth preserving as-is
point to EDW augmentation; an unbearable EDW maintenance window points to
lake-as-staging; a from-scratch build for a technical user base points to
all-in-one. All three are explicitly migration paths, not just architecture
choices — the point of naming them separately from the destination MDW is
that each has its own known evolution route into one.
