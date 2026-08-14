---
type: concept
title: Kimball versus Inmon Architecture
description: The trade-off between the Kimball bus architecture, built on conformed dimensions, and the Inmon/CIF hub-and-spoke architecture, built on a normalized enterprise warehouse.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 1, 16"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 2"
  - title: "Deciphering Data Architectures"
    resource: "Deciphering Data Architectures (James Serra), ch. 8"
---

Both approaches agree that enterprise-wide integration matters; they disagree on the mechanism.

## Independent (stand-alone) data mart architecture

Departments, or a single subject area, build an analytic database on their own, in isolation, with no enterprise context: operational systems feed ETL that loads the mart directly, reflecting that group's own business rules and labeling, dimensional or otherwise. It is often the fastest, cheapest path to visible results, since it sidesteps the work of reconciling cross-functional definitions of shared entities like customer or product — and it proliferates for legitimate reasons beyond simple lack of discipline: purchased packaged applications and their add-ons, legacy systems that predate a later enterprise commitment, shadow-IT builds outside the IT department, and marts inherited via mergers and acquisitions.

Its problems surface once *more than one* such mart exists side by side: redundant ETL hitting the same source systems, different technologies and query infrastructures per mart (earning the pejorative label "stovepipe"), duplicated technology/process/skillset costs, and — most seriously — no shared repository for granular data, so a mart may be unable to answer a future question needing more detail than originally anticipated, and comparing data across marts may be impossible or actively misleading if they don't share consistent definitions of common entities, or if redundant load processes apply different business rules to the same source data. Marts built this way become "islands of information." It is strongly discouraged at enterprise scale — wasteful long-term and productive of incompatible views that require ongoing debate and reconciliation — even though it often does use dimensional modeling for ease of use and performance; its failure mode is disregarding [conformed dimensions](conformed-dimensions.md) and atomic, [business process](business-process.md)-centric design, not dimensional modeling itself. A single stand-alone data mart can still be a sound choice, as long as the organization has a shared, explicit understanding of the future cost/rework trade-off it is accepting if it later needs to integrate with other marts.

### Coping with a stand-alone mart's lack of conformance

Because stand-alone marts lack enterprise context by definition, and pull directly from operational systems, they are near-universal in practice (departmental investment, M&A, packaged applications) despite being widely criticized. Once one exists, or a decision is made to build one anyway, three coping strategies address its lack of conformance with the rest of the environment:

- **Live with the incompatibility** — an informed, jointly-made business decision (IT, business, and executive stakeholders together), made with a clear-eyed understanding of the costs in plain business terms: inability to compare processes without future redevelopment, redundant IT maintenance, and disputes from competing data representations.
- **Conform "along the way"** — a commonly self-deceiving plan ("build Sales now, adjust when we get to Inventory") that underestimates the effort of retrofitting dimensions already in production. A more realistic middle path expands the current project's scope just for the dimensions likely to have enterprise implications — fully developing those against all their operational sources and broader business requirements, not just the current subject area's needs — without committing to a full enterprise conformance strategy phase up front.
- **Retrofit the dimensions later** — viable once a [conformed dimensions](conformed-dimensions.md) bulwark exists elsewhere and a legacy mart needs to join it. On paper this is three steps: map each nonconforming row to its enterprise-model counterpart, add any attributes missing from the enterprise model, and reassign the mart's fact table foreign keys to the now-conforming dimension. In practice it understates the real difficulty — rows may not map one-to-one because of differing entity definitions or differing [slowly changing dimension](slowly-changing-dimension.md) histories that require source-data reconciliation rather than simple mapping, and every dependent front-end artifact (queries, reports, dashboards, filters) requires redevelopment against the new structure and content.

## Hub-and-spoke Corporate Information Factory (CIF) architecture (Inmon)

Data is extracted and processed through an ETL layer into a normalized (3NF) **Enterprise Data Warehouse (EDW)** — mandatory in CIF, versus only optional as an ETL staging convenience in the [Kimball DW/BI architecture](kimball-dw-bi-architecture.md). CIF relies on the normalized EDW to deliver enterprise integration; Kimball relies instead on the [enterprise data warehouse bus architecture](enterprise-data-warehouse-bus-architecture.md) and its [conformed dimensions](conformed-dimensions.md). The core critique: normalization does not by itself speak to integration — separate, incompatible database sources can be normalized to the hilt without addressing integration at all, since normalization only removes redundancy within one schema. The Kimball architecture reverses this logic, resolving data inconsistencies directly through conformed dimensions, without requiring normalization as a prerequisite.

Downstream from the EDW, dimensionally structured analytic databases are typically built, but they usually differ from a proper Kimball presentation area by being departmentally centric (not process-centric) and aggregated rather than atomic; extra business rules applied in this downstream ETL step can make it hard to tie the results back to the EDW. The most extreme, pure form of CIF is considered unworkable as a data warehouse architecture: it locks atomic data inside difficult-to-query normalized structures while still delivering departmentally incompatible data marts to different groups of business users — reproducing the independent-data-mart failure mode one layer downstream, and expecting business users to query normalized atomic data directly compounds the problem, since aggregating strips away the dimensionality that made the atomic data valuable in the first place.

## Hybrid hub-and-spoke and Kimball architecture

Populates a CIF-centric EDW that is completely off-limits to business users, used solely as a clean source to populate a Kimball-style dimensional, atomic, process-centric presentation area conforming to the bus architecture. This can leverage a pre-existing normalized investment while offloading query performance and usability entirely to the dimensional layer. It's a reasonable path if an existing 3NF EDW isn't delivering fast, flexible reporting on its own; starting from scratch, the hybrid costs more time and money than going directly to a dimensional presentation area, due to redundant data movement and storage — pursue it only with the budget and organizational patience for full normalization ahead of dimensional loading.

## A third variant: Data Vault as the hub-and-spoke layer

[Data Vault](data-vault-versus-dimensional-modeling.md) is a more recent alternative to a 3NF EDW for the hub-and-spoke storage layer, purpose-built for auditability and for absorbing new sources and changing relationships without redesign. Like the CIF hybrid above, it is typically paired with a dimensional presentation layer downstream rather than exposed to business users directly.

## Common misconceptions about the two methodologies

Several persistent claims about this trade-off don't hold up:

- **"Kimball is purely bottom-up with no enterprise-wide focus."** False — the [enterprise data warehouse bus matrix](enterprise-data-warehouse-bus-matrix.md) *is* Kimball's top-down element: a deliberate, up-front architectural blueprint of the organization's business processes and their conformed dimensions. What's genuinely bottom-up is the execution against that blueprint — building one business process's star at a time — not the absence of enterprise planning.
- **"Inmon requires a fully designed enterprise warehouse before anything can be built (a big-bang or waterfall approach)."** False — Inmon has consistently advocated against a big-bang build, explicitly naming it as the most critical failure mode to avoid; his own writing describes each new data mart adding only the incremental data it needs to an already-growing CIF, not waiting on a complete upfront design. Both methodologies reserve real time for upfront design before iterating, and neither sits at either extreme of the ad-hoc-versus-waterfall spectrum.
- **"Inmon's architecture doesn't allow star-schema data marts."** False — Inmon's own later writing endorses star-schema data marts specifically as a good way to give end users direct, understandable access to CIF data; the disagreement between the two methodologies is about what integrates the marts (a normalized EDW versus conformed dimensions), not about whether marts themselves should be dimensional.
- **"The two approaches are incompatible and must be chosen between."** False — see the hybrid architecture above; a normalized EDW layer and a Kimball-style conformed dimensional presentation layer can and often do coexist, each doing the job it's best suited for.

The practical implication for a design decision: don't reject a hybrid or don't assume either methodology dictates all-or-nothing behavior on these specific points — evaluate the actual trade-off (normalized-EDW-mediated integration versus conformed-dimension-mediated integration, described above) rather than a caricature of either side.
