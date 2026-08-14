---
type: concept
title: Vendor-Neutral Discovery Questionnaire
description: >
  A fixed list of product- and cloud-agnostic questions, each mapped to a
  specific architectural implication, keeps early data-architecture
  discovery from anchoring on a vendor before the requirements that should
  drive the choice are known.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (James Serra), ch. 3"
---

A vendor-neutral discovery questionnaire is a fixed set of questions, none
of which names a specific product or cloud provider, asked during the
discovery phase of a data-architecture engagement (see [Architecture
Design Session](architecture-design-session.md)). It is the concrete
operationalization of [architecture before tool
selection](architecture-before-tool-selection.md) at the level of a single
conversation: every question is chosen so it can be answered without
reference to any vendor, and each answer maps onto a specific architectural
implication, so the architecture is shaped by requirements and constraints
before any product or cloud-provider preference enters the discussion.
Product and provider preferences are asked about and mapped onto the
already-shaped architecture afterward, not before.

Representative questions and what they drive, illustrating the pattern
rather than an exhaustive list: whether any source data is nonrelational
(determines whether a data lake is needed at all); data volume (drives
storage and partitioning design, to avoid slow queries later); presence
and velocity of streaming sources (determines which ingestion components
are needed); usage pattern — dashboards versus ad hoc queries, batch
versus interactive (drives both product choice and the [fit
criteria](fit-criterion.md) response time must hit); report SLAs (a
millisecond versus minute requirement changes not just product choice but
how many redundant copies of the data are needed to hit it); high
availability and disaster recovery targets, i.e. RTO/RPO (most cloud
providers cover typical HA needs by default, but a stated RTO/RPO can force
major architectural additions); data-residency or PII handling
requirements arising from customer contracts (can force multiple,
geographically separated data lakes, or an anonymization strategy); need
for 24/7 access (forces eliminating maintenance-window downtime in every
component, not just one); concurrent-user counts at peak (some products
cap concurrency, ruling them out or forcing composition with another
product); end-user skill level (low skill favors no-code/low-code
products; mentioning a code-heavy option to a non-technical audience gets
a blank stare and wastes the conversation); budget (large budgets remove
constraints, small budgets force explicit trade-offs, e.g. less compute
for slower loading); and project timeline (a long build warrants checking
with the provider about unannounced upcoming products, so the project
doesn't start on something about to be superseded).

Each question is also a [mandated constraint](mandated-constraint.md) or
[non-functional requirement](non-functional-requirement.md) probe in
disguise: "how fast do reports need to run" elicits a fit criterion; "what
is your budget" elicits a mandated constraint; "any data-sovereignty
requirements" elicits a constraint that can override an otherwise-preferred
design. Running through the fixed list systematically catches
architecturally consequential answers that a free-form conversation would
likely miss, the same value a [context-free interview
template](context-free-interview-template.md) provides for general
requirements interviews — this is that same discipline specialized to data
architecture, with each question pre-annotated by the architectural
consequence of the likely answers rather than left generic.
